#def big_mac(): 
#    print("sanduiche big mac")

#print("Inicio")
#big_mac()
#print("Fim")

def fazer_big_mac(nome):
    print(f"sanduiche big mac {nome}")

#fazer_big_mac("Roger")
#fazer_big_mac("Cris")
#fazer_big_mac("Manu")   

def fazer_batata(tamanho):
     print(f"batata {tamanho}")

def preparar_refrigerante(tipo,tamanho):
     print(f"{tipo} {tamanho}")

fazer_big_mac("Felipe")
fazer_batata("Grande")
preparar_refrigerante("Coca","Média")         

def fazer_combo_big_mac(nome,tamanho_batata,tipo_refri,tamanho_refri):
     fazer_big_mac(nome)
     fazer_batata(tamanho_batata)
     preparar_refrigerante(tipo_refri,tamanho_refri)

fazer_combo_big_mac("Felps", "Grande", "Coca cola", "Grande")

