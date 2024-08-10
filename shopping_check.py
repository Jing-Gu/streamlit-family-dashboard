import streamlit as st
import functions

todos = functions.get_todos("todos.txt")
todos_completed = functions.get_todos("todos_completed.txt")


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    if new_todo:
        todos.append(new_todo)
        functions.write_todos(todos, "todos.txt")
        st.session_state["new_todo"] = ""   # clear the input field


def delete_todos():
    st.session_state.todos = []
    st.session_state.todos_completed = []
    functions.write_todos(st.session_state.todos, "todos.txt")
    functions.write_todos(st.session_state.todos_completed, "todos_completed.txt")
    st.toast("Your shopping list is cleared!")


st.title("Shopping List 🛒")
st.write("Another todo app but not coded in JS")

if todos:
    st.subheader("What to buy:")
    for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=f"todo_{index}")
        if checkbox:
            completed = todos.pop(index)
            todos_completed.append(completed)
            functions.write_todos(todos, "todos.txt")
            functions.write_todos(todos_completed, "todos_completed.txt")
            # Reinitialize state after updating
            st.session_state.todos = todos
            st.session_state.todos_completed = todos_completed
            st.rerun()
else:
    st.write("Your shopping list is empty. 🤷")

st.text_input(label="", placeholder="Something to buy?",
              on_change=add_todo, key="new_todo")

if todos or todos_completed:
    st.button("Clear the list", on_click=delete_todos)

if todos_completed:
    st.subheader("Already bought:")
    for index, todo_c in enumerate(todos_completed):
        checkbox = st.checkbox(todo_c, key=f"todo_c_{index}", value=True)
        if checkbox is False:
            uncompleted = todos_completed.pop(index)
            todos.append(uncompleted)
            functions.write_todos(todos, "todos.txt")
            functions.write_todos(todos_completed, "todos_completed.txt")
            del st.session_state[todo_c]
            st.rerun()





