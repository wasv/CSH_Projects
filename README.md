# CSH Project Management System

A system for CSH to manage, track, and document house projects. In addition, the system will serve as a way to recruit members onto projects based on skillset and interests.

## My Ideas
* Links to external websites related to project (GitHub, Wiki, etc).
* Integrated build-log and/or documentation system.
* Profile of skills and projects.
* Search for members with specific skills, or projects that need a certain skill.
* Lists or tags such as 'eboard picks' or 'freshmen projects'

## Navigation Breakdown
* Index - List of all active projects and concepts.
* Limbo - List of inactive projects.
* Project Details - Comments, links to external sites, and list of owner and collaborator profile.
* Profile - List of users projects, bio, resume, and links

## Model Breakdown
* Projects
  * Title (v1)
  * Description (v1)
  * Last Update (v1)
  * Owner (v1)
  * Collaborators (v2)
  * Picture (v1.5)
  * Links (v1.5)
  * State (Concept/Active/Inactive/Done) (v2)
    * Project is a 'Concept' until there is a physical object or compilable code.
    * Project is 'Active' if owner/collaborator 'Checks in' every 2 months.
    * Considered 'inactive' if no check in after 1 year or explicitly abandoned.
      * Allow new owner to 'revive' project? (or maybe 'fork' it instead?)
    * Project can be marked as 'Done' when there is no need for further updates.
  * Suggestions/Comments (v2)
  * Build Updates (v2)
* Profiles
  * Name (v1)
  * Bio (v1)
  * List of projects (v1)
  * Picture (v1.5)
  * Links to social networks (v1.5)
  * Resume (v2)
* Skills (v3?)

## UPDATE: 15-09-15 Redesign Based on R&D Suggestions
* Less PMS, more Project Board.
* List of projects/ideas, with suggestions and comments.
* Include build log feature?

* Profiles from webauth for comments.
* Link to LinkedIn? See Y$
* Allow uploading resume to profile.
