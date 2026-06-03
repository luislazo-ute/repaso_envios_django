CREATE USER luis_envios_user WITH PASSWORD 'admin123';
CREATE DATABASE luis_envios_db OWNER luis_envios_user;

\c luis_envios_db

ALTER SCHEMA public OWNER TO luis_envios_user;
GRANT ALL ON SCHEMA public TO luis_envios_user;
GRANT CREATE ON SCHEMA public TO luis_envios_user;

ALTER DEFAULT PRIVILEGES FOR USER luis_envios_user IN SCHEMA public
GRANT ALL ON TABLES TO luis_envios_user;

ALTER DEFAULT PRIVILEGES FOR USER luis_envios_user IN SCHEMA public
GRANT ALL ON SEQUENCES TO luis_envios_user;

ALTER DEFAULT PRIVILEGES FOR USER luis_envios_user IN SCHEMA public
GRANT ALL ON FUNCTIONS TO luis_envios_user;