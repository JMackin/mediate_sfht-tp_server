A drupal server for connecting a web interface (nginx) with an sftp server(OpenSSH).
Intended to be deployed in a docker container.

----

Hypothetical structure:

```
                                 [ - docker - ]
     { client }  -- request-->   |  [[nginx]  |   -- rev-proxy--
                                                               /
                                  [      - docker -     ]     /                       
                                  | [[gunicorn (wsgi)]] | <--    
                                  | | [[drupal (py)]] | |
       [   - docker -   ]                        /           
       |  [[ssh_tunn]]  |  <--paramiko (SFTP) --
       |       \\       |
       |  [[sftp_serv]] |
                    \\
                       ===>  { server } 

```
