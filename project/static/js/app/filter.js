app.filter('timeago', function () {
    return function (input) {
        return $.timeago(input);
    };
});

app.filter('bbcode', function ($sce, BBCode) {
    return function (input) {
        var html = BBCode.render(input);
        return $sce.trustAsHtml(html);
    }
});

// app.filter('bbcodeTags', function () {
//     return function (input) {
//         return input.replace(/\B#(\w+)/gi, '[url=/blog/tag/$1]#$1[/url]');
//     }
// });
