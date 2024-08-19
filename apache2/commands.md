# enable site command 
    ```
        a2ensite <name of site to enable>
    ```

    example:
    ```
        a2ensite example1.net
    ```

# disable sites

    ```
        a2dissite <name of site to disable>
    ```

# enable modules

    ```
        a2enmod
    ```

# test apache config files
    ```
    apachectl configtest
    ```

# list enabled modules
```
apachectl -M
```

# Status module
## Enabling
```
a2enmod status
```