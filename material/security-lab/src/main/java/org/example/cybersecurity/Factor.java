package org.example.cybersecurity;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Factor {
    public static String run(String input) {
        if (input.isEmpty()) {
            return "Syntax: /math?factorize=<integer>";
        }

        // Intentionally vulnerable: the user input is concatenated into a shell
        // command. This allows remote code execution (RCE). This is the point of
        // the lab. Never build a command line from untrusted input in real code.
        ProcessBuilder processBuilder = new ProcessBuilder();
        String cmd = "/usr/bin/factor '" + input + "'";
        System.out.println("COMMAND: " + cmd);
        processBuilder.command("bash", "-c", cmd);

        StringBuilder output = new StringBuilder();
        try {
            Process process = processBuilder.start();
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return output.toString();
    }
}
