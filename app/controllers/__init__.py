
fruit_columns = ['id_fruit', 'name', 'id_region']

fruit_table = '''
    "id_fruit" BIGSERIAL CONSTRAINT pk_fruit PRIMARY KEY,
    "name" VARCHAR(20) CONSTRAINT un_fruit UNIQUE NOT NULL,
    "id_region" SERIAL NOT NULL,
    CONSTRAINT fk_region FOREIGN KEY ("id_region") REFERENCES region ("id_region")
'''


region_columns = ['id_region', 'name']
region_table = '''
    "id_region" SERIAL CONSTRAINT pk_region PRIMARY KEY,
    "name" VARCHAR(20) CONSTRAINT un_region UNIQUE NOT NULL,
    "status" BOOLEAN CONSTRAINT df_region DEFAULT true
'''

