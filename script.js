Java.perform(function() {
    var okhttp3 = Java.use('okhttp3.OkHttpClient');

    okhttp3.newCall.overload('okhttp3.Request').implementation = function(request) {
        var url = request.url().toString();
        var method = request.method();

        send({url: url, method: method});

        return this.newCall(request);
    };
});
