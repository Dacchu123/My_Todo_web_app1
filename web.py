import streamlit as st
import functions
import os

if not os.path.exists("todo output.txt"):
    with open("todo output.txt", "w") as file:
        pass

todos = functions.get_todos()


def add_todo():
    new = st.session_state["new_todo"]
    todos.append(new + "\n")
    functions.write_todos(todos)


st.title("Hey My Todo App")
st.subheader("THis is my todo app")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo:  ", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
