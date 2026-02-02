let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

// Afegeix comptador a tasques existents (compatibilitat versions anteriors)
tasks = tasks.map(task => ({
    ...task,
    count: typeof task.count === 'number' ? task.count : 1
}));

// Carrega les tasques al inici
displayTasks();

// Event listeners
document.getElementById('addBtn').addEventListener('click', addTask);
document.getElementById('taskInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        addTask();
    }
});

function addTask() {
    const input = document.getElementById('taskInput');
    const text = input.value.trim();

    if (text === '') {
        alert('Escriu una tasca!');
        return;
    }

    const duplicate = tasks.some(task => task.text.toLowerCase() === text.toLowerCase());
    if (duplicate) {
        alert('Aquesta tasca ja existeix!');
        return;
    }

    // Afegir nova tasca
    tasks.push({
        id: Date.now(),
        text: text,
        completed: false,
        count: 1
    });

    saveTasks();
    displayTasks();
    input.value = '';
}

function deleteTask(id) {
    tasks = tasks.filter(task => task.id !== id);
    saveTasks();
    displayTasks();
}

function toggleTask(id) {
    const task = tasks.find(t => t.id === id);
    if (task) {
        task.completed = !task.completed;
        saveTasks();
        displayTasks();
    }
}

function incrementCount(id) {
    const task = tasks.find(t => t.id === id);
    if (task) {
        task.count += 1;
        saveTasks();
        displayTasks();
    }
}

function decrementCount(id) {
    const task = tasks.find(t => t.id === id);
    if (task && task.count > 0) {
        task.count -= 1;
        saveTasks();
        displayTasks();
    }
}

function saveTasks() {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

// Mostra les tasques a la pantalla
function displayTasks() {
    const taskList = document.getElementById('taskList');
    
    if (tasks.length === 0) {
        taskList.innerHTML = '<li class="empty">No tens tasques pendents!</li>';
        return;
    }

    taskList.innerHTML = tasks.map(task => `
        <li class="${task.completed ? 'completed' : ''}" data-task-id="${task.id}">
            <div class="task-main">
                <span class="task-text">${task.text}</span>
                <div class="counter">
                    <button class="counter-btn decrement" data-task-id="${task.id}">-</button>
                    <span class="count">${task.count}</span>
                    <button class="counter-btn increment" data-task-id="${task.id}">+</button>
                </div>
            </div>
            <div class="actions">
                <button class="delete-btn" data-task-id="${task.id}">🗑️</button>
            </div>
        </li>
    `).join('');
    
    // Event listeners
    document.querySelectorAll('.counter-btn.increment').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            incrementCount(parseInt(this.dataset.taskId));
        });
    });
    
    document.querySelectorAll('.counter-btn.decrement').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            decrementCount(parseInt(this.dataset.taskId));
        });
    });
    
    document.querySelectorAll('.delete-btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            deleteTask(parseInt(this.dataset.taskId));
        });
    });
    
    document.querySelectorAll('li').forEach(li => {
        li.addEventListener('dblclick', function(e) {
            if (!e.target.classList.contains('counter-btn') && !e.target.classList.contains('delete-btn')) {
                toggleTask(parseInt(this.dataset.taskId));
            }
        });
    });
}
