-- Script that creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE p_id INT;

    -- Intentamos obtener el ID del proyecto si ya existe
    SELECT id INTO p_id FROM projects WHERE name = project_name;

    -- Si el proyecto no existe (p_id es NULL), lo creamos
    IF p_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET p_id = LAST_INSERT_ID();
    END IF;

    -- Insertamos la corrección
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, p_id, score);
END$$
DELIMITER ;
