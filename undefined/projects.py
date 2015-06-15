
class _Projects:
    """A _project_ represents a prioritized list of tasks in Asana. It exists in a
    single workspace or organization and is accessible to a subset of users in
    that workspace or organization, depending on its permissions.
    
    Projects in organizations are shared with a single team. You cannot currently
    change the team of a project via the API. Non-organization workspaces do not
    have teams and so you should not specify the team of project in a
    regular workspace."""

    def __init__(self, client=None):
        self.client = client
  
    def create(self, params={}, **options): 
        """Creates a new project in a workspace or team.
        
        Every project is required to be created in a specific workspace or
        organization, and this cannot be changed once set. Note that you can use
        the `workspace` parameter regardless of whether or not it is an
        organization.
        
        If the workspace for your project _is_ an organization, you must also
        supply a `team` to share the project with.
        
        Returns the full record of the newly created project.

        Parameters
        ----------
        data : Object
          Data for the request
        workspace : Id
          The workspace or organization to create the project in.
        team : Id
          If creating in an organization, the specific team to create the
          project in.
        """
        
        return self.client.post("/projects", params, **options)
        
  
    def create_in_workspace(self, workspace, params={}, **options): 
        """If the workspace for your project _is_ an organization, you must also
        supply a `team` to share the project with.
        
        Returns the full record of the newly created project.

        Parameters
        ----------
        workspace : Id
          The workspace or organization to create the project in.
        data : Object
          Data for the request
        """
        
        path = "/workspaces/%d/projects" % (workspace)
        return self.client.post(path, params, **options)
        
  
    def create_in_team(self, team, params={}, **options): 
        """Creates a project shared with the given team.
        
        Returns the full record of the newly created project.

        Parameters
        ----------
        team : Id
          The team to create the project in.
        data : Object
          Data for the request
        """
        
        path = "/teams/%d/projects" % (team)
        return self.client.post(path, params, **options)
        
  
    def find_by_id(self, project, params={}, **options): 
        """Returns the complete project record for a single project.

        Parameters
        ----------
        project : Id
          The project to get.
        params : Object
          Parameters for the request
        """
        
        path = "/projects/%d" % (project)
        return self.client.get(path, params, **options)
        
  
    def update(self, project, params={}, **options): 
        """A specific, existing project can be updated by making a PUT request on the
        URL for that project. Only the fields provided in the `data` block will be
        updated; any unspecified fields will remain unchanged.
        
        When using this method, it is best to specify only those fields you wish
        to change, or else you may overwrite changes made by another user since
        you last retrieved the task.
        
        Returns the complete updated project record.

        Parameters
        ----------
        project : Id
          The project to update.
        data : Object
          Data for the request
        """
        
        path = "/projects/%d" % (project)
        return self.client.put(path, params, **options)
        
  
    def delete(self, project, params={}, **options): 
        """A specific, existing project can be deleted by making a DELETE request
        on the URL for that project.
        
        Returns an empty data record.

        Parameters
        ----------
        project : Id
          The project to delete.
        """
        
        path = "/projects/%d" % (project)
        return self.client.delete(path, params, **options)
        
  
    def find_all(self, params={}, **options): 
        """Returns the compact project records for some filtered set of projects.
        Use one or more of the parameters provided to filter the projects returned.

        Parameters
        ----------
        params : Object
          Parameters for the request
        workspace : Id
          The workspace or organization to filter projects on.
        team : Id
          The team to filter projects on.
        archived : Boolean
          Only return projects whose `archived` field takes on the value of
          this parameter.
        """
        
        return self.client.get_collection("/projects", params, **options)
        
  
    def find_by_workspace(self, workspace, params={}, **options): 
        """Returns the compact project records for all projects in the workspace.

        Parameters
        ----------
        workspace : Id
          The workspace or organization to find projects in.
        params : Object
          Parameters for the request
        archived : Boolean
          Only return projects whose `archived` field takes on the value of
          this parameter.
        """
        
        path = "/workspaces/%d/projects" % (workspace)
        return self.client.get_collection(path, params, **options)
        
  
    def find_by_team(self, team, params={}, **options): 
        """Returns the compact project records for all projects in the team.

        Parameters
        ----------
        team : Id
          The team to find projects in.
        params : Object
          Parameters for the request
        archived : Boolean
          Only return projects whose `archived` field takes on the value of
          this parameter.
        """
        
        path = "/teams/%d/projects" % (team)
        return self.client.get_collection(path, params, **options)
        
  
