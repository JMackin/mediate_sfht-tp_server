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

    - cd mediate_http-sftp/mediator/

    - export SCRTS_MAPPINGS="scrts/mappings"
    - export PLCS_MAPPINGS="places/mappings"
    - export DJANGO_SETTINGS_MODULE=mediator.settings

Running Gunicorn:

    - cd mediate_http-sftp/mediator/

    - gunicorn mediator_wsgi.wsgi_connector:WsgiConnector

Mappings files:\
There are two files required for 'places' and 'scrts'. These are JSON files that the program uses as reference to
the storage <b>locations</b> of files containing required values and configurations. \
Listed below are their formats which need to be populated with the host-specific values.

- Key-files and password-files:


    # scrts/mappings

    {
        "key_loc": {
            "django_key": "<SECRET_KEY>",
            "gpg-s": "<apps private GPG-key>",
            "gpg-p": "<apps public GPG-key>",
            "sftp-p": "<apps public SSH key>",
            "sftp-s": "<apps private SSH key>"
        },
        "key_pwd": {
            "sftp-s": "<app's private SSH key password>",
            "gpg-s": "<app's  private GPG key password>"
        },
        "users": {
            "sftp-user": "<SSH login name for SFTP client-worker>"
        },
        "hosts": {
            "sftp-serv": "<SSH login name for SFTP host-worker>"
        }
    }

- Entity (i.e client/server) configurations


    # places/mappings

    {
      "place_locations": {
        "client": "<client-config values>",
        "server": "<server-config values>"
      }
    }


Since this project is still very early I will return another time to document the
files pointed to in the latter...
