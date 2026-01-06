package com.todo.alexandru;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@SpringBootApplication
@RestController
@CrossOrigin(origins = "*") // permite cereri de oriunde
public class Main {

    private final TaskRepository taskRepository;

    public Main(TaskRepository taskRepository){
        this.taskRepository = taskRepository;
    }

    public static void main(String[] args){
        SpringApplication.run(Main.class, args);
    }

    @GetMapping("/")
    public String hello(){
        return "Hello, World!";
    }

    @GetMapping("/tasks")
    public List<Task> getTasks(){
        return taskRepository.findAll();
    }

    record NewTaskRequest(
            String titlu,
            String descriere
    ){}

    @PostMapping("/add-task")
    public void addTask(@RequestBody NewTaskRequest request){
        Task task = new Task();
        task.setTitlu(request.titlu());
        task.setDescriere(request.descriere());
        taskRepository.save(task);
    }

    @DeleteMapping("/delete/{id}")
    public void deleteTask(@PathVariable("id") Integer id){
        taskRepository.deleteById(id);
    }

}
