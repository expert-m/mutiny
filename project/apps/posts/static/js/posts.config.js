app.config(function ($routeProvider) {
    $routeProvider.when('/post/:id/', {
        templateUrl: '/static/html/posts.detail.html',
        controller: PostCtrl,
        resolve: PostCtrl.resolve
    });
});