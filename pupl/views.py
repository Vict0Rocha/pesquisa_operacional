# pulp/views.py

from django.shortcuts import render, redirect
import pulp
import re

# Imports para geração de gráficos
import matplotlib
matplotlib.use('Agg') # Configura o Matplotlib para não usar interface gráfica
import matplotlib.pyplot as plt
import numpy as np
import io
import base64


def home_view(request):
    if request.method == 'GET':
        return render(request, 'home.html')

    if request.method == 'POST':
        try:
            data = request.POST
            
            # --- 1. Extrair e validar variáveis ---
            variables_info = {}
            for key in data:
                match = re.match(r'var_name_(\d+)', key)
                if match:
                    var_id = match.group(1)
                    var_name = data[key].strip().replace(" ", "_") # Remove espaços
                    if not var_name:
                        continue # Pula variáveis sem nome

                    variables_info[var_id] = {
                        'name': var_name,
                        'type': data.get(f'var_type_{var_id}'),
                        'obj_coef': float(data.get(f'obj_coef_{var_name}', 0))
                    }

            if not variables_info:
                raise ValueError("Nenhuma variável de decisão válida foi definida.")

            # --- 2. Montar o problema PuLP ---
            prob = pulp.LpProblem(data.get('problem_name', 'DynamicProblem'), 
                                  pulp.LpMaximize if data.get('objective_type') == 'max' else pulp.LpMinimize)

            pulp_vars = {
                info['name']: pulp.LpVariable(info['name'], lowBound=0, cat=info['type'])
                for info in variables_info.values()
            }

            prob += pulp.lpSum(info['obj_coef'] * pulp_vars[info['name']] for info in variables_info.values()), "Objective"
            
            # --- 3. Extrair e adicionar restrições ---
            constraints_info = {} # ... (lógica de extração de restrições continua a mesma)
            # ... (cole a sua lógica de extração de restrições aqui, ela já é robusta)
            for key in data:
                match = re.match(r'const_(\d+)_rhs', key)
                if match:
                    const_id = match.group(1)
                    if const_id not in constraints_info:
                        constraints_info[const_id] = {'coeffs': {}, 'name': f"Restricao_{const_id}"}
                    
                    constraints_info[const_id]['rhs'] = float(data[key])
                    constraints_info[const_id]['op'] = data.get(f'const_{const_id}_op')

                    for var_name in pulp_vars.keys():
                        coef_key = f'const_{const_id}_coef_{var_name}'
                        if coef_key in data and data[coef_key]:
                            constraints_info[const_id]['coeffs'][var_name] = float(data[coef_key])

            for const_id, info in constraints_info.items():
                expression = pulp.lpSum(info['coeffs'].get(name, 0) * var for name, var in pulp_vars.items())
                if info['op'] == '<=': prob += expression <= info['rhs'], info['name']
                elif info['op'] == '>=': prob += expression >= info['rhs'], info['name']
                else: prob += expression == info['rhs'], info['name']

            # --- 4. Resolver e preparar resultados ---
            prob.solve()
            
            results = {
                'problem_name': prob.name,
                'status': pulp.LpStatus[prob.status],
                'objective_value': pulp.value(prob.objective),
                'variables': [{'name': v.name, 'value': v.varValue} for v in prob.variables()],
                'constraints_analysis': [],
                'plot_url': None
            }

            # --- 5. Análise de Sensibilidade (Slack e Shadow Price) ---
            if results['status'] == 'Optimal':
                for name, c in prob.constraints.items():
                    results['constraints_analysis'].append({
                        'name': name,
                        'slack': c.slack,
                        'shadow_price': c.pi
                    })

            # --- 6. Geração de Gráfico para problemas de 2 variáveis ---
            if len(pulp_vars) == 2 and results['status'] == 'Optimal':
                # (A lógica de geração de gráfico será adicionada aqui)
                # ... (veja o código completo abaixo)
                # pulp/views.py (continuação do home_view)

                if len(pulp_vars) == 2 and results['status'] == 'Optimal':
                    var_names = list(pulp_vars.keys())
                    x_var, y_var = pulp_vars[var_names[0]], pulp_vars[var_names[1]]
                    
                    # Encontrar um limite razoável para os eixos do gráfico
                    max_val = max(v['value'] for v in results['variables']) * 2.5
                    max_val = max(max_val, 10) # Garante um valor mínimo
                    
                    x_vals = np.linspace(0, max_val, 400)
                    plt.figure(figsize=(8, 7))
                    
                    # Plotar as retas das restrições
                    for const in constraints_info.values():
                        coeffs = const['coeffs']
                        x_coeff = coeffs.get(x_var.name, 0)
                        y_coeff = coeffs.get(y_var.name, 0)
                        rhs = const['rhs']
                        
                        if y_coeff != 0:
                            y_vals = (rhs - x_coeff * x_vals) / y_coeff
                            plt.plot(x_vals, y_vals, label=f"{const['name']}")
                        elif x_coeff != 0:
                            plt.axvline(x=rhs/x_coeff, linestyle='--', label=f"{const['name']}")

                    # Ponto ótimo
                    optimal_x = results['variables'][0]['value']
                    optimal_y = results['variables'][1]['value']
                    plt.scatter(optimal_x, optimal_y, color='red', s=100, zorder=5, label=f"Ótimo ({optimal_x:.2f}, {optimal_y:.2f})")

                    plt.xlabel(x_var.name)
                    plt.ylabel(y_var.name)
                    plt.title(f"Região Viável e Solução Ótima para '{prob.name}'")
                    plt.legend()
                    plt.grid(True)
                    plt.xlim(0, max_val)
                    plt.ylim(0, max_val)

                    # Salvar gráfico em memória
                    buf = io.BytesIO()
                    plt.savefig(buf, format='png')
                    buf.seek(0)
                    # Codificar para passar ao template
                    results['plot_url'] = base64.b64encode(buf.getvalue()).decode('utf-8')
                    plt.close()


            request.session['pulp_results'] = results

        except (ValueError, TypeError) as e:
            request.session['pulp_error'] = f"Erro nos dados de entrada. Verifique se todos os números são válidos. Detalhe: {e}"
        except Exception as e:
            request.session['pulp_error'] = f"Ocorreu um erro inesperado: {e}"

        return redirect('results')


def results_view(request):
    context = {
        'results': request.session.get('pulp_results', None),
        'error': request.session.get('pulp_error', None),
    }
    # Limpa a sessão
    if 'pulp_results' in request.session: del request.session['pulp_results']
    if 'pulp_error' in request.session: del request.session['pulp_error']
    
    return render(request, 'results.html', context)