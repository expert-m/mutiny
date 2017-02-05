app.config(function ($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: '/static/html/index.main.html',
        controller: IndexCtrl,
        resolve: IndexCtrl.resolve
    });
});
