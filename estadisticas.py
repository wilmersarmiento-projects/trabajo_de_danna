import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sr = pd.read_csv('SalesReport.csv')

agrupado = sr.groupby('item_name')['quantity'].sum()
agrupadobarraslabel = agrupado.index
coloresbarra = sns.color_palette("viridis", n_colors=len(agrupado))

plt.bar(agrupado.index, agrupado.values, color=coloresbarra)
plt.xlabel('Item Name')
plt.ylabel('Cantidad total')
plt.title('Cantidad total pedida por item')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("graficobarras.png")

sr['date'] = sr['date'].str.replace('-', '/') 
sr['date'] = pd.to_datetime(sr['date'], errors='coerce', dayfirst=True)

# 1. Ventas totales por tipo de ítem

colorespie = sns.color_palette("viridis", n_colors=2)
ventas_por_tipo = sr.groupby('item_type')['transaction_amount'].sum()
porcentajes = ventas_por_tipo.values
nombres = ventas_por_tipo.index

# Gráfico 1: Ventas totales por tipo de ítem

plt.figure(figsize=(8,5))
plt.pie(porcentajes, labels=nombres, colors=colorespie, startangle=0, autopct='%1.1f%%')
plt.title("Ingresos por tipo de ítem")
plt.tight_layout()
plt.savefig("ingresosporitem.png")


# 2. Cantidad total vendida por ítem
cantidad_por_item = sr.groupby('item_name')['quantity'].sum().reset_index()

# Gráfico 2: Cantidad total vendida por ítem (top 10)

plt.figure(figsize=(10,6))
top_items = cantidad_por_item.sort_values(by='quantity', ascending=False).head(10)
sns.barplot(data=top_items, x='item_name', y='quantity', palette='magma')
plt.title('Top 7 Items mas vendidos')
plt.ylabel('Cantidad total vendida')
plt.xlabel('Nombre del item')
plt.xticks(rotation=75)
plt.tight_layout()
plt.savefig("ventasporitem.png")

# 3. Número de transacciones por tipo de transacción

transacciones_tipo = sr['transaction_type'].value_counts().reset_index()
transacciones_tipo.columns = ['transaction_type', 'conteo']

# Gráfico 3: Conteo de transacciones por tipo

plt.figure(figsize=(6,4))
sns.barplot(data=transacciones_tipo, x='transaction_type', y='conteo', palette='coolwarm')
plt.title('Número de Transacciones por Tipo')
plt.ylabel('Cantidad de Transacciones')
plt.xlabel('Tipo de Transacción')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("transaccionesportipo.png")

# 4. Ventas totales por fecha

ventas_por_fecha = sr.groupby('date')['transaction_amount'].sum().reset_index()

# Gráfico 4: Evolución de ventas por fecha

plt.figure(figsize=(12,5))
sns.lineplot(data=ventas_por_fecha, x='date', y='transaction_amount')
plt.title('Ventas Totales por Fecha')
plt.ylabel('Monto Total de Ventas')
plt.xlabel('Fecha')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("ventasporfecha.png")

# 5. Comparación ventas mujeres y hombres

ventas_por_genero = sr.groupby('received_by')['quantity'].sum().reset_index()
coloresventaporgenero = ['blue', 'magenta']

# Gráfico 5: Comparación ventas mujeres y hombres

plt.figure(figsize=(5,5))
sns.barplot(data=ventas_por_genero, x='received_by', y='quantity', palette=coloresventaporgenero, width=0.5)
plt.title('Ventas Totales por Genero')
plt.ylabel('Ventas totales')
plt.xlabel('Genero')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("ventasporgenero.png")
