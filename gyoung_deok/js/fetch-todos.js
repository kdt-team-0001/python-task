fetch("https://jsonplaceholder.typicode.com/todos")
    .then((response) => response.json())
    .then((json) => {
        json.forEach((todo) => {
            todoPrint(todo);
        });
    });

function todoPrint(todo){
    let result = `{\n\tuserId: ${todo.userId},\n\tid: ${todo.id},\n\ttitle: ${todo.title},\n\tcompleted: ${todo.completed ? '완료' : '미완료'}\n}`
    console.log(result)
}