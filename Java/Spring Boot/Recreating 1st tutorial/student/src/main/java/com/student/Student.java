package com.student;

import jakarta.persistence.*;

import java.util.Objects;

@Entity
public class Student {

    @Id
    @SequenceGenerator(
            name = "student_id_sequence",
            sequenceName = "student_id_sequence",
            allocationSize = 1
    )
    @GeneratedValue(
            strategy = GenerationType.SEQUENCE,
            generator = "student_id_sequence"
    )

    private Integer id;
    private String nume;
    private String prenume;
    private String email;
    private Integer an;
    private Integer medie;

    public Student(Integer id, String nume, String prenume, String email, Integer an, Integer medie) {
        this.id = id;
        this.nume = nume;
        this.prenume = prenume;
        this.email = email;
        this.an = an;
        this.medie = medie;
    }

    public Student(){
    }

    public String getPrenume() {
        return prenume;
    }

    public void setPrenume(String prenume) {
        this.prenume = prenume;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Integer getAn() {
        return an;
    }

    public void setAn(Integer an) {
        this.an = an;
    }

    public Integer getMedie() {
        return medie;
    }

    public void setMedie(Integer medie) {
        this.medie = medie;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Student student = (Student) o;
        return Objects.equals(id, student.id) && Objects.equals(nume, student.nume) && Objects.equals(prenume, student.prenume) && Objects.equals(email, student.email) && Objects.equals(an, student.an) && Objects.equals(medie, student.medie);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, nume, prenume, email, an, medie);
    }

    @Override
    public String toString() {
        return "Student{" +
                "id=" + id +
                ", nume='" + nume + '\'' +
                ", prenume='" + prenume + '\'' +
                ", email='" + email + '\'' +
                ", an=" + an +
                ", medie=" + medie +
                '}';
    }
}
