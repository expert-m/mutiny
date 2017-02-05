app.config(function ($routeProvider) {
    $routeProvider.when('/users/', {
        templateUrl: '/static/html/users.list.html',
        controller: UsersCtrl,
        resolve: UsersCtrl.resolve
    });

    $routeProvider.when('/user/:id/', {
        templateUrl: '/static/html/users.detail.html',
        controller: UserCtrl,
        resolve: UserCtrl.resolve
    });

    $routeProvider.when('/user/:id/edit/', {
        templateUrl: '/static/html/users.edit.html',
        controller: UserEditCtrl,
        resolve: UserEditCtrl.resolve
    });

    $routeProvider.when('/register/', {
        templateUrl: '/static/html/users.register.html',
        controller: UserRegisterCtrl
    });
});