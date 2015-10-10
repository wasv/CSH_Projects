# CSH Project Management System Design Description

A system for CSH to manage, track, and document house projects. In addition, the system will serve as a way to recruit members onto projects based on skillset and interests.

## My Ideas
* Links to external websites related to project (GitHub, Wiki, etc).
* Integrated build-log and/or documentation system.
* Profile of skills and projects.
* Search for members with specific skills, or projects that need a certain skill.
* Lists or tags such as 'eboard picks' or 'freshmen projects'

## Navigation Breakdown
* Project Lists - List of projects based on status.
* Project Details - Description, links to external sites, and link to owner profile.
* Profile - List of users projects, bio, resume, and links.

## Model Breakdown
* Projects
  * Title
  * Description
  * Last Update
  * Owner
  * Picture
  * Links
  * State (Concept/Active/Inactive/Done)
    * Project is a 'Concept' until there is a physical object or compilable code.
    * Project is 'Active' if owner/collaborator 'Checks in' every 2 months.
    * Considered 'inactive' if no check in after 1 year or explicitly abandoned.
      * Allow new owner to 'revive' project? (or maybe 'fork' it instead?)
    * Project can be marked as 'Done' when there is no need for further updates.
  * Collaborators (Not Used)
  * Suggestions/Comments (Planned)
  * Build Updates (Planned)
* Profiles
  * Name
  * Bio
  * List of projects
  * Picture
  * Link to website
  * Resume (Planned)
* Skills (Planned)