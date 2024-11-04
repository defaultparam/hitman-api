# Hitman Ideas

- Create a hitman db api... get a list of all targets and their information and sum it up in an API
- Create a completionist app which lists all challenges from destination... so one can research how to complete challenges away
	- Also fetch the api for user to see which challenges have been already completed.

Missions: Represents each mission in the game.
        Mission Objectives: Specific tasks or goals within each mission.
        Side Gigs: Optional tasks or additional objectives within missions.
        Challenges: Optional challenges that players can complete in each mission.

Targets: Characters that Agent 47 interacts with or eliminates.
    NPCs (Non-Playable Characters): Other characters that populate the missions.

Locations: Different places where missions occur.

Weapons/Tools: Items that Agent 47 can use during missions.
    Disguises: Outfits or disguises available to Agent 47.

===========

Models required:

    - Characters : Contains character profile, attributes, tags, occupation, relation to other characters etc properties like diana, agent 47

        - Could be targets, could be friendly

    - Locations: To map the missions and target locations. 

        - This will only be used to reference target / mission locations and can be used to sort targets into groups

    - Items: Just a feature of the API to collect all the items such as weapons, tools etc.

# end goals

- Track challenges / Compleitionist app

- Hitman Planner (offline plan for missions)

- Build a hitman app giving the feel of hitman universe in phone.
