var IndexCtrl = function ($scope, $rootScope, posts) {
    $rootScope.title = '42 BUGS :: Главная';
    $scope.posts = posts.results;
};

IndexCtrl.resolve =  {
    posts: function (api) {
        return api('posts').getPage(0, 10);
    }
};

app.controller('IndexCtrl', IndexCtrl);
