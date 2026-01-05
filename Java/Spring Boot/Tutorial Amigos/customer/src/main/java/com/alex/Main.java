package com.alex;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Objects;

@SpringBootApplication
@RestController
@RequestMapping("/api/v1/customers")
public class Main {

    private final CustomerRepository customerRepository;

    public Main(CustomerRepository customerRepository){
        this.customerRepository = customerRepository;
    }

    public static void main(String[] args){
        SpringApplication.run(Main.class, args);
    }

    @GetMapping
    public List<Customer> getCustomer(){
        return customerRepository.findAll();
    }

    record NewCustomerRequest(
            String name,
            String email,
            Integer age
    ){

    }

    @PostMapping
    public void addCustomer(@RequestBody NewCustomerRequest request){
        Customer customer = new Customer();
        customer.setName(request.name());
        customer.setEmail(request.email());
        customer.setAge(request.age());
        customerRepository.save(customer);
    }



    @DeleteMapping("{customerId}")
    public void deleteCustomer(@PathVariable("customerId") Integer id){
        customerRepository.deleteById(id);
    }












//    @GetMapping("/")
//    public GreetResponse greet(){
//        return new GreetResponse("Hey!");
//    }

    class GreetResponse{
        private final String greet;

        public GreetResponse(String greet){
            this.greet = greet;
        }

        public String getGreet(){
            return this.greet;
        }

        @Override
        public String toString(){
            return "GreetRespone{" +
                    "greet='" + greet + '\'' +
                    "}";
        }

        //alt + fn + insert
        @Override
        public boolean equals(Object o) {
            if (o == null || getClass() != o.getClass()) return false;
            GreetResponse that = (GreetResponse) o;
            return Objects.equals(greet, that.greet);
        }

        @Override
        public int hashCode() {
            return Objects.hashCode(greet);
        }
    }

}

