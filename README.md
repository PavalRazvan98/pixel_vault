# Pixel Vault(像素库)
This project represent a library for gaming. I chose this kind of library because gaming is a passion of mine.
On this web page you can create an account, review a game, and you can also add games, developers, publishers and many 
other specification to you're desire games.

## Tech stack
In this app I used the followings tech:
1. Developed using **Python** & **Django**;
2. Tested using **pytest** and **faker**;
3. Linted with **ruff**;

## Custom Management Commands

* ping: Warning! This command is used only for debug purposes and doesn't do anything
* populate_misc_database: Populate the "misc" database
* populate_games_database: Populate the "games" database.
* populate_feedback_database: Populate the "feedback" database.
* populate_interaction_database: Populate the "interaction" database.
* populate_users_database: Populate the database with 15 fake users.
* create_pixel_vault_superuser: Create a superuser using the command flags, otherwise use the environment variables. Check the config section for the info regarding environment variables.
* populate_database: Call the commands: populate_misc_database, populate_games_database, populate_feedback_database, populate_interaction_database.

## Configuration

| Config name                | Type  | Default Value   | Description                             |
|----------------------------|-------|-----------------|-----------------------------------------|
| PIXEL_VAULT_USERNAME       | str   | admin           | Default value for Super User `Username` |
| PIXEL_VAULT_PASSWORD       | str   | qwerty123       | Default value for Super User `Password` |
| PIXEL_VAULT_EMAIL          | str   | admin@gmail.com | Default value for Super User `Email`    |
| PIXEL_VAULT_SECRET_KEY     | str   | ***             | ???                                     |
| POSTGRES_USER              | str   | postgres        | Postgres account username               |
| POSTGRES_PASSWORD          | str   | postgres        | Postgres account password               |
| POSTGRES_DB                | str   | pixel_vault     | Postgres Database name                  |
| POSTGRES_PORT              | str   | 55432           | The port that Postgres use              |
| POSTGRES_HOST              | str   | 127.0.0.1       | The host that Postgres use              |