# xxh-plugin-local-example
<p align="center">
  Fork this to create xxh local plugin that will run before or after an xxh connection is established on the local host.
</p>

<p align="center">
If you like the idea of xxh click ⭐ on the repo and stay tuned.
</p>

## Install
From xxh repo:
```bash
xxh +I https://github.com/grg121/xxh-plugin-local-example

```
Connect:
```
xxh yourhost
```

## Local plugins

This kind of xxh plugin is intended to run additional steps on local machine previous or after the xxh remote connection.

You could fork this repo and add additional scripts that will be run before and after xxh connection, the scripts must follow the pattern "post_connect-*py" or "pre_connect-*py".