# Format String vulnerability

This challenge is to use an attacker-controlled format string, plus attacker controlled input, to write arbitrary data (in this case a specific four-byte integer) onto the stack.

Once the magic value is written, the flag is printed out.

### Flag

LBCTF{4lw4y5_sp3c1fy_y0ur_f0rm4t_sp3c1f13r}

### Building

make, gcc, and Docker need to be installed.
Run `make` at the command line to make it (on Linux)


You can check that the challenge works locally by changing LOCAL to True in exploit.py and running
exploit.py. You will need to run `pip3 install pwntools` for it to run, but if you get the flag back you should be fine.


Build the Docker container:

```bash
# docker build . -t format
# docker run -p 1234:1234 format
```

Now if you can change LOCAL to False in exploit.py and run it again, you should still get the flag.

### Deployment

After deploying the challenge, the competitors should have access to student.c. **DON'T** give them access to format.c - it has the flag.

### Vulnerability

printf() and other functions that accept a format string argument should not take that argument from a user. Like %d for numbers and %s for strings, there is %n and %hn that let you store the number of characters printed at a particular location. If the user gets printf to output 255 characters, they can use %hn to write 255 to a particular place.

In this case, the exploit is writing twice using %hn. It writes first half of the "authenticated" variable, and then the second half two bytes after that in memory (2 + 2 = 4 byte integer).
