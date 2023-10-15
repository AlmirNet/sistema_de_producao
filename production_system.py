import sqlite3
from datetime import datetime

conn = sqlite3.connect('production_orders.db')
cursor = conn.cursor()

def add_production_order(product_name, quantity, delivery_date):
    try:
        # Verificar disponibilidade de materiais
        if not ckeck_material_availability(product_name, quantity):
            print("Não há materiais suficientes para produzir esta ordem.")
            return
        
        # Inserir a ordem no banco de dados
        cursor.execute("INSERIR INTO production_orders (product_name, quantity, delivery_date, status) VALUE (?, ?, ?, ?)",(product_name, quantity, delivery_date, "Em andamento"))

        conn.commit()
        print("Ordem de produção adicionada com sucesso.")
    except Exception as e:
        print("Erro ao adicionar a ordem de produção:", str(e))

def list_production_orders():
    cursor.excecute("SELECT * FROM production_orders")
    orders = cursor.fetchall()
    if orders:
        for order in orders:
            print("ID:", order[0])
            print("Produto:", order[1])
            print("Quantidade", order[2])
            print("Data de Entrega:", order[3])
            print("Status", order[4])
            print("\n")
        else:
            print("Nenhuma ordem de produção encontrda.")

def ckeck_material_availability(product_name, quantity):
    # Implementando a lógica para Verificar a disponibilidade de materiais.
    # Retornando True se houver materiais suficientes, False caso contrário.
    return True

def update_order_status(order_id, status):
    try:
        cursor.execute("UPDATE production_orders SET status = ? WHERE order_id = ?", (status, order_id))
        conn.commit()
        print("Status ordem de produção atualizado com sucesso.")
    except Exception as e:
        print("Erro ao atualizar o status de produção:", str(e))

def generate_production_report():
    cursor.execute("SELECT * FROM production_orders WHERE status = 'Em andamento'")
    in_progress = cursor.fetchall()
    cursor.execute("SELECT * FROM production_orders WHERE status = 'Concluída'")
    completed = cursor.fetchall()

    print("Ordens em andamento:")
    for order in in_progress:
        print(f"ID: {order[0]}, Produto: {order[1]}, Quantidade: {order[2]}")

    print("\nOrdens concluídas:")
    for order in completed:
        print(f"ID: {order[0]}, Produto: {order[1]}, Quantidade: {order[2]}")

if __name__ == '__main__':
    while