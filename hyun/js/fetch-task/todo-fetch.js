// 완료된 할일(todo) 개수와 미완료된 할일 개수 출력하기

fetch("https://jsonplaceholder.typicode.com/todos")
    .then((response) => response.json())
    .then((todos) => countByStatus(todos));

function countByStatus(todos) {
    const countArray = [0, 0];
    todos.forEach((todo) => {
        if (todo.completed) countArray[0]++;
        else countArray[1]++;
    });
    console.log(`완료된 할일 개수: ${countArray[0]}`);
    console.log(`미완료된 할일 개수: ${countArray[1]}`);
}
