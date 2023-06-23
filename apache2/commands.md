1. enable site command 
    ```
        a2ensite <name of site to enable>
    ```

    example:
    ```
        a2ensite example1.net
    ```

2. disable sites

    ```
        a2dissite <name of site to disable>
    ```

3. enable modules

    ```
        a2enmod
    ```

4. test apache config files
    ```
    apachectl configtest
    ```