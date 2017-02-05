app.config(function ($routeProvider) {
    $routeProvider.when('/projects/', {
        templateUrl: '/static/html/projects.list.html',
        controller: ListProjectsCtrl,
        resolve: ListProjectsCtrl.resolve
    });
});