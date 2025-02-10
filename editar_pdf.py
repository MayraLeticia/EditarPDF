import fitz  

# Abrir o PDF
doc = fitz.open("junho.pdf")

# Texto a substituir
texto_antigo = "01/05/2025"
texto_novo = "06/05/2025"

date_mapping = {
    "01/05/2025": "01/06/2025",
    "02/05/2025": "02/06/2025",
    "03/05/2025": "03/06/2025",
    "04/05/2025": "04/06/2025",
    "05/05/2025": "05/06/2025",
    "06/05/2025": "06/06/2025",
    "07/05/2025": "07/06/2025",
    "08/05/2025": "08/06/2025",
    "09/05/2025": "09/06/2025",
    "10/05/2025": "10/06/2025",
    "11/05/2025": "11/06/2025",
    "12/05/2025": "12/06/2025",
    "13/05/2025": "13/06/2025",
    "14/05/2025": "14/06/2025",
    "15/05/2025": "15/06/2025",
    "16/05/2025": "16/06/2025",
    "17/05/2025": "17/06/2025",
    "18/05/2025": "18/06/2025",
    "19/05/2025": "19/06/2025",
    "20/05/2025": "20/06/2025",
    "21/05/2025": "21/06/2025",
    "22/05/2025": "22/06/2025",
    "23/05/2025": "23/06/2025",
    "24/05/2025": "24/06/2025",
    "25/05/2025": "25/06/2025",
    "26/05/2025": "26/06/2025",
    "27/05/2025": "27/06/2025",
    "28/05/2025": "28/06/2025",
    "29/05/2025": "29/06/2025",
    "30/05/2025": "30/06/2025",
    "31/05/2025": "31/06/2025"
}

week_mapping = {
    "5ª Feira": "Domingo",
    "6ª Feira": "2ª Feira",
    "Sábado": "3ª Feira",
    "Domingo": "4ª Feira",
    "2ª Feira": "5ª Feira",
    "3ª Feira": "6ª Feira",
    "4ª Feira": "Sábado"
}

# Percorre cada página
for page_num, page in enumerate(doc):
    for texto_antigo, texto_novo in date_mapping.items():
        text_instances = page.search_for(texto_antigo)  # Procura pelo texto na página

    
        if text_instances:  # Se o texto for encontrado
            print(f"Texto encontrado na página {page_num + 1}, substituindo...")

            for inst in text_instances:
                rect = fitz.Rect(inst)  # Obtém a posição do texto
                
                # 🧼 Cobre completamente a área do texto antigo com um retângulo branco
                page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1), overlay=True)

                # 📝 Reescreve o novo texto exatamente na mesma posição
                page.insert_text(
                    (rect.x0 + 4 , rect.y0 + 7.5 ),
                    texto_novo,
                    fontsize=9, 
                    color=(0, 0, 0),  # Vermelho, pode mudar para preto (0,0,0)
                    overlay=True
                )

    for texto_antigo, texto_novo in week_mapping.items():
        text_instances = page.search_for(texto_antigo)  # Procura pelo texto na página

    
        if text_instances:  # Se o texto for encontrado
            print(f"Texto encontrado na página {page_num + 1}, substituindo...")

            for inst in text_instances:
                rect = fitz.Rect(inst)  # Obtém a posição do texto
                
                # 🧼 Cobre completamente a área do texto antigo com um retângulo branco
                page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1), overlay=True)

                # 📝 Reescreve o novo texto exatamente na mesma posição
                page.insert_text(
                    (rect.x0 + 4 , rect.y0 + 7.5 ),
                    texto_novo,
                    fontsize=9, 
                    color=(0, 0, 0),  # Vermelho, pode mudar para preto (0,0,0)
                    overlay=True
                )
            break

# Salvar o novo PDF
doc.save("junho_editado.pdf")
doc.close()

print("Novo PDF salvo como 'junho_editado.pdf'")
