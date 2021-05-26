# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
#couldn't create foreign key for the Fact Table  'songplays'

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY, \
                                        start_time BIGINT REFERENCES time(start_time), \
                                        user_id int REFERENCES users(user_id), \
                                        level varchar NULL, \
                                        song_id varchar REFERENCES songs(song_id), \
                                        artist_id varchar REFERENCES artists(artist_id), \
                                        session_id int NOT NULL, \
                                        location varchar NULL, \
                                        user_agent varchar NULL);
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY, \
                                    first_name varchar NULL, \
                                    last_name varchar NULL, \
                                    gender varchar NULL, \
                                    level varchar NULL); 
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, \
                                    title varchar NULL, \
                                    artist_id varchar NULL, \
                                    year int NULL, \
                                    duration float NULL); \
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY, \
                                        name varchar NULL, \
                                        location varchar NULL, \
                                        latitude float NULL, \
                                        longitude float NULL ); \
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (start_time BIGINT PRIMARY KEY, \
                                    hour int NOT NULL, \
                                    day int NOT NULL, \
                                    week int NOT NULL, \
                                    month int NOT NULL, \
                                    year int NOT NULL, \
                                    weekday int NOT NULL); 
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (songplay_id, \
                            start_time, \
                            user_id, \
                            level, \
                            song_id, \
                            artist_id, session_id, location, \
                            user_agent)
    VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
    INSERT INTO users (user_id, \
                        first_name, \
                        last_name, \
                        gender, \
                        level)
    VALUES (%s, %s, %s,%s, %s) on conflict (user_id) do update set level = EXCLUDED.level
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, \
                        title, \
                        artist_id, \
                        year, \
                        duration)
    VALUES (%s, %s, %s,%s, %s)
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, \
                        name, \
                        location, \
                        latitude, \
                        longitude)
    VALUES (%s, %s, %s,%s, %s) on conflict do nothing
""")


time_table_insert = ("""
    INSERT INTO time (start_time, \
                        hour, \
                        day, \
                        week, \
                        month, \
                        year, \
                        weekday) 
    VALUES (%s, %s, %s,%s, %s,%s, %s) on conflict do nothing
""")

# FIND SONGS

song_select = ("""
                    SELECT songs.song_id, artists.artist_id 
                    FROM artists 
                    JOIN songs ON songs.artist_id = artists.artist_id 
                    WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s;

""")

# QUERY LISTS

create_table_queries = [ user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]