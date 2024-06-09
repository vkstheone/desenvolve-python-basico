import emoji

print("Emojis disponíveis:")
print(f"❤️ - :red_heart:")
print(f"👍 - :thumbs_up:")
print(f"🤔 - :thinking_face:")
print(f"🥳 - :partying_face:")

frase_codificada = input("\nDigite uma frase e ela será emojizada:\n")

frase_emojizada = emoji.emojize(frase_codificada)

print("\n Frase emojizada:")
print(frase_emojizada)