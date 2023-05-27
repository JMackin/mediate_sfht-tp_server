A django server for connecting a web interface (nginx) with an sftp server(OpenSSH).
Intended to be deployed in a docker container.

----

Hypothetical structure:

```
                                 [ - docker - ]
     { client }  -- request-->   |  [[nginx]  |   -- rev-proxy--
                                                               /
                                  [      - docker -     ]     /                       
                                  | [[gunicorn (wsgi)]] | <--    
                                  | | [[django (py)]] | |
       [   - docker -   ]                        /           
       |  [[ssh_tunn]]  |  <--paramiko (SFTP) --
       |       \\       |
       |  [[sftp_serv]] |
                    \\
                       ===>  { server } 

```

Dealing with env variables:
    To make work:

    - cd mediate_htt-sftp/mediator/
    - export SCRTS_MAPPINGS="scrts/mappings"
    - export PLCS_MAPPINGS="places/mappings"
    - export DJANGO_SETTINGS_MODULE=mysite.settings

running Gunicorn
    
    - gunicorn mediator_wsgi.wsgi_connector:WsgiConnector
