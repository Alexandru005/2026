package com.student;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@SpringBootApplication
@RestController
public class Main {
    private final StudentRepository studentRepository;

    public Main(StudentRepository studentRepository){
        this.studentRepository = studentRepository;
    }

    public static void main(String[] args){
        SpringApplication.run(Main.class, args);
    }

    //Default
    @GetMapping("/")
    public String greet(){
        return "Hello!";
    }

    @GetMapping("/students")
    public List<Student> getStudents(){
        return studentRepository.findAll();
    }



    record NewStudentRequest(
            String nume,
            String prenume,
            String email,
            Integer an,
            Integer medie
    ){

    }

    @PostMapping("/add-student")
    public void addStrudent(@RequestBody NewStudentRequest request){
        Student student = new Student();
        student.setNume(request.nume());
        student.setPrenume(request.prenume());
        student.setEmail(request.email());
        student.setAn(request.an());
        student.setMedie(request.medie());
        studentRepository.save(student);
    }

    @DeleteMapping("/delete-student{studentId}")
    public void deleteStudent(@PathVariable("studentId") Integer id){
        studentRepository.deleteById(id);
    }


}
