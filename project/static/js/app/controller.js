app.controller('MainCtrl', function ($scope, $rootScope, ui, $window, apiAuth, apiProfile, api) {
    $scope.auth_user = {};
    $scope.auth_user.remember_me = true;

    /* FUNC */

    $scope.userName = function (user, short) {
        if (!user) return;
        if (user.first_name) {
            var name = user.first_name;
            if (user.last_name)
                name += ' ' + user.last_name;
            if (!short)
                name += ' (' + user.username + ')';
            return name;
        }

        return user.username;
    };

    /* PAGE CHANGE */

    $rootScope.$on('$routeChangeStart', function () {
        ui.progress.start();
        $rootScope.leftBlock = true;
        $rootScope.pageLoading = true;
    });

    $rootScope.$on('$routeChangeSuccess', function () {
        ui.progress.done();
        $rootScope.pageLoading = false;
    });

    /* TOASTER */

    $window.$.toaster({
        settings: {
            timeout: 5000,
            toaster: {
                css: {
                    left: '12px',
                    top: 'none',
                    bottom: '12px'
                }
            },
            toast: {
                // template: '<div class="alert alert-%priority% alert-dismissible" role="alert">' +
                // '<button type="button" class="close" data-dismiss="alert">' +
                // '<span aria-hidden="true">&times;</span>' +
                // '<span class="sr-only">Закрыть</span>' +
                // '</button>' +
                // '<span class="message"></span>' +
                // '</div>',

                template: '<div class="toast toast-%priority%" role="toast">' +
                '<span class="message"></span>' +
                '</div>',
                css: {
                    'margin-bottom': '0',
                    'margin-top': '12px'
                },
                remove: function ($toast, callback) {
                    return $toast.animate(
                        { opacity: '0' },
                        { complete: callback }
                    );
                }
            }
        }
    });

    /* AUTH */

    apiProfile.get().then(function (data) {
        $rootScope.user = data;
    });

    $scope.login = function (data) {
        apiAuth.login(data).then(function (data) {
            $rootScope.user = data;
            ui.alert('Успешная авторизация', 'success');
        });
    };

    $scope.logout = function () {
        apiAuth.logout().then(function () {
            $rootScope.user = undefined;
        });
    };

    /* TAGS */
    api('tags').getPage(0, 50).then(function (data) {
        $scope.tags = data.results;
    });
});

app.controller('404Ctrl', function ($scope, $rootScope) {
    $rootScope.title = '404';
    $rootScope.leftBlock = false;
});