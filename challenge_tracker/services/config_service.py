import sqlite3
from uuid import UUID
from ..models.challenge import Challenge
from ..models.dtos.challenge_create_dto import ChallengeCreateRequest
from ..models.dtos.challenge_update_dto import ChallengeUpdateRequest
import json

class ConfigService:
    def __init__(self, db_path="database.db"):
        self.db_path = db_path
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        # Create a table if it doesn't exist
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS challenges (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                image TEXT,
                is_completed BOOLEAN NOT NULL CHECK (is_completed IN (0, 1)),
                category TEXT,
                destination TEXT,
                rewards TEXT,
                available_in TEXT,
                additional_properties TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def create_challenge(self, challenge: ChallengeCreateRequest):
        # Insert a new challenge record
        conn = self._connect()
        cursor = conn.cursor()
        _challenge = challenge.to_challenge()
        cursor.execute('''
            INSERT INTO challenges (id, title, description, image, is_completed, category, destination, rewards, available_in, additional_properties)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            str(_challenge.id), 
            _challenge.title, 
            _challenge.description, 
            _challenge.image,
            _challenge.is_completed, # default to be false
            _challenge.category.value, 
            _challenge.destination.value,
            str(_challenge.rewards),
            _challenge.available_in,
            str(_challenge.additional_properties)
        ))

        conn.commit()
        conn.close()

        return _challenge.id

    def update_challenge(self, challenge_id: UUID, challenge: ChallengeUpdateRequest):
        # Update an existing challenge
        conn = self._connect()
        cursor = conn.cursor()
    
        # Prepare the SQL statement dynamically based on provided fields
        update_fields = []
        update_values = []
    
        # Mapping of fields to their SQL representation
        field_mapping = {
            "title": "title = ?",
            "description": "description = ?",
            "image": "image = ?",
            "category": "category = ?",
            "destination": "destination = ?",
            "rewards": "rewards = ?",
            "available_in": "available_in = ?",
            "additional_properties": "additional_properties = ?"
        }
    
        for field, sql_repr in field_mapping.items():
            value = getattr(challenge, field)
            if value is not None:
                update_fields.append(sql_repr)
                if field == "rewards":
                    update_values.append(str(value))
                elif field in {"category", "destination"}:
                    update_values.append(value.value)
                else:
                    update_values.append(value)
    
        # Add the challenge_id for the WHERE clause
        update_values.append(str(challenge_id))
    
        # Construct the final SQL statement
        if update_fields:
            sql = f"UPDATE challenges SET {', '.join(update_fields)} WHERE id = ?"
            cursor.execute(sql, update_values)
    
        conn.commit()
        conn.close()


    def delete_challenge(self, challenge_id: UUID):
        # Delete a challenge by ID
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM challenges WHERE id = ?', (str(challenge_id),))
        conn.commit()
        conn.close()

    def get_challenge(self, challenge_id: UUID):
        # Fetch a single challenge by ID
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM challenges WHERE id = ?', (str(challenge_id),))
        result = cursor.fetchone()
        conn.close()

        if result:
            # Define the columns in the same order as they are in the table
            columns = [
                "id", "title", "description", "image", "is_completed", 
                "category", "destination", "rewards", "available_in", "additional_properties"
            ]
            # Create a dictionary from the result and column names
            result_dict = dict(zip(columns, result))
            # Return as a JSON string
            return result_dict
        return None

    def get_all_challenges(self) -> []:
        # Fetch all challenges from the database
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM challenges')
        results = cursor.fetchall()
        conn.close()

        if results:
            # Define the columns in the same order as they are in the table
            columns = [
                "id", "title", "description", "image", "is_completed", 
                "category", "destination", "rewards", "available_in", "additional_properties"
            ]
            challenges = []
            # Create a dictionary from the result and column names  
            for result in results:
                challenges.append(dict(zip(columns, result)))
            # Return as a JSON string
            return challenges
        return []
