if __name__ == "__main__":
    todo_list = []
    redo_list = []
    
    def show_list(lista):
        print("\nTarefas adicionadas: \n")
        for v in lista:
            print(v)
            
    def add_list(task, lista):
        print("Tarefa adicionada")
        lista.append(task)
    
    while True:
        todo = input("Digite uma tarefa para adicionar à lista ou uma das seguintes opções [undo, redo, ls]: ")
        
        if todo == "ls":
            show_list(todo_list)
            continue
        elif todo == "undo":
            ...
            continue
        elif todo == "redo":
            ...
            continue
        add_list(todo, todo_list)