import redis
import psycopg2
from psycopg2.extras import RealDictCursor

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Connect to PostgreSQL
db_connection = psycopg2.connect(
    dbname='your_db',
    user='your_user',
    password='your_password',
    host='localhost',
    port='5432'
)

class SkillCachePortfolio:
    @staticmethod
    def retrieve_user_portfolio(user_id):
        # Try to get data from cache
        cached_portfolio = redis_client.get(f'portfolio:{user_id}')
        if cached_portfolio:
            return cached_portfolio.decode('utf-8')
        
        # If not in cache, get data from database
        cursor = db_connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM portfolios WHERE user_id = %s", (user_id,))
        portfolio = cursor.fetchone()
        
        if portfolio:
            # Store the result in cache and return it
            redis_client.set(f'portfolio:{user_id}', str(portfolio))
            return portfolio
        else:
            return "Portfolio not found"

class SkillCacheSkills:
    @staticmethod
    def add_skill(user_id, skill_name):
        # Add skill to the database
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO skills (user_id, skill_name) VALUES (%s, %s)", (user_id, skill_name))
        db_connection.commit()
        
        # Invalidate the cache entry for the user's skills
        redis_client.delete(f'skills:{user_id}')
        return "Skill added successfully"

    @staticmethod
    def retrieve_user_skills(user_id):
        # Try to get data from cache
        cached_skills = redis_client.get(f'skills:{user_id}')
        if cached_skills:
            return cached_skills.decode('utf-8')
        
        # If not in cache, get data from database
        cursor = db_connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT skill_name FROM skills WHERE user_id = %s", (user_id,))
        skills = cursor.fetchall()
        
        if skills:
            # Store the result in cache and return it
            redis_client.set(f'skills:{user_id}', str(skills))
            return skills
        else:
            return "No skills found"

class SkillCacheProjects:
    @staticmethod
    def retrieve_user_projects(user_id):
        # Try to get data from cache
        cached_projects = redis_client.get(f'projects:{user_id}')
        if cached_projects:
            return cached_projects.decode('utf-8')
        
        # If not in cache, get data from database
        cursor = db_connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM projects WHERE user_id = %s", (user_id,))
        projects = cursor.fetchall()
        
        if projects:
            # Store the result in cache and return it
            redis_client.set(f'projects:{user_id}', str(projects))
            return projects
        else:
            return "Projects not found"

    @staticmethod
    def add_user_project(user_id, project):
        # Add project to the database
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO projects (user_id, project) VALUES (%s, %s)", (user_id, project))
        db_connection.commit()
        
        # Invalidate the cache entry for the user's projects
        redis_client.delete(f'projects:{user_id}')
        return "Project added successfully"

# Example Usage
if __name__ == "__main__":
    # Adding data
    print(SkillCachePortfolio.add_user_portfolio("user123", "My Portfolio"))
    print(SkillCacheSkills.add_skill("user123", "Python"))
    print(SkillCacheSkills.add_skill("user123", "JavaScript"))
    print(SkillCacheProjects.add_user_project("user123", "Project 1"))
    print(SkillCacheProjects.add_user_project("user123", "Project 2"))

    # Retrieving data
    print(SkillCachePortfolio.retrieve_user_portfolio("user123"))
    print(SkillCacheSkills.retrieve_user_skills("user123"))
    print(SkillCacheProjects.retrieve_user_projects("user123"))

    # Retrieving non-existent data
    print(SkillCachePortfolio.retrieve_user_portfolio("user456"))
    print(SkillCacheSkills.retrieve_user_skills("user456"))
    print(SkillCacheProjects.retrieve_user_projects("user456"))
