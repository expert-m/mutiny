var UsersCtrl = function ($scope, $rootScope, users) {
    $rootScope.title = '42 BUGS :: Участники';
    $scope.users = users.results;
};

UsersCtrl.resolve = {
    users: function (api) {
        return api('users').getPage(0, 50);
    }
};

app.controller('UsersCtrl', UsersCtrl);


var UserCtrl = function ($scope, $rootScope, profile) {
    $scope.profile = profile;
    $rootScope.title = profile.username;
};

UserCtrl.resolve = {
    profile: function (api, $route) {
        return api('users').getObject($route.current.params.id);
    }
};

app.controller('UserCtrl', UserCtrl);


var UserEditCtrl = function ($scope, $rootScope, profile) {
    $rootScope.title = 'Редактирование профиля';
    $scope.profile = profile;
};

UserEditCtrl.resolve = {
    profile: function (api, $route) {
        return api('users').getObject($route.current.params.id);
    }
};

app.controller('UserEditCtrl', UserEditCtrl);


var UserRegisterCtrl = function ($rootScope) {
    $rootScope.title = '42 BUGS :: Регистрация';
};

app.controller('UserRegisterCtrl', UserRegisterCtrl);