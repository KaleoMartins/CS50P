nome = input("Nome do arquivo: ").strip().lower()
if nome.endswith(".gif"):
    print("image/gif")
elif nome.endswith(".jpg") or nome.endswith(".jpeg"):
    print("image/jpeg")
elif nome.endswith(".png"):
    print("image/png")
elif nome.endswith(".pdf"):
    print("application/pdf")
elif nome.endswith(".txt"):
    print("text/plain")
elif nome.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")