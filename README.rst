==================
Discord-Bot-Docker
==================

This package provides a basic discord bot as docker package.

- Build docker image

.. code::

    docker build -t devanshshukla99/discord_bot:latest .

- Run docker image

.. code::

    docker run -d \
    --name=bot \
    -e PUID=1000 \
    -e PGID=1000 \
    -e TOKEN=[discord_bot_token] \
    --restart unless-stopped \
    devanshshukla99/discord_bot:latest

Here the ``discord_bot_token`` must be obtained via the discord's developer portal.

License
-------
This plugin is licenced under an ``MIT`` licence - see the ``LICENSE`` file.
