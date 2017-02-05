app.config(function ($routeProvider) {
    $routeProvider.when('/meetings/', {
        templateUrl: '/static/html/meetings.list.html',
        controller: ListMeetingsCtrl,
        resolve: ListMeetingsCtrl.resolve
    });
});