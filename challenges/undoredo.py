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
        
    def do_undo(todo_list, redo_list):
        if not todo_list:
            print("Nenhuma ação anterior a desfazer.")
            return
        last_todo = todo_list.pop()
        redo_list.append(last_todo)
    
    def do_redo(todo_list, redo_list):
        if not redo_list:
            print("Nenhuma ação para refazer.")
        try:
            last_redo = todo_list.pop()
            todo_list.append(last_redo)
        except IndexError:
            pass
    
    while True:
        todo = input("Digite uma tarefa para adicionar à lista ou uma das seguintes opções [undo, redo, ls]: ")
        
        if todo == "ls":
            show_list(todo_list)
            continue
        elif todo == "undo":
            do_undo(todo_list, redo_list)
            continue
        elif todo == "redo":
            do_redo(todo_list, redo_list)
            continue
        add_list(todo, todo_list)