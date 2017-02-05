var ListProjectsCtrl = function ($scope, $timeout, ui, projects) {
    $scope.projects = projects.results;
};

ListProjectsCtrl.resolve = {
    projects: function (api) {
        return api('projects').getPage(0, 50);
    }
};

app.controller('ListProjectsCtrl', ListProjectsCtrl);
