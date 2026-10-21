package org.example.cybersecurity;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class FactorController {
    @RequestMapping(value = "/math")
    String math(@RequestParam(defaultValue = "") String factorize) {
        return Factor.run(factorize);
    }
}
