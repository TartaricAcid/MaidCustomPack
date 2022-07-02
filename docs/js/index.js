var vm = new Vue({
    el: '#modelpack',
    data() {
        return {
            info: 'null',
            index: 0,
            all: [],
            maid: [],
            chair: [],
            sound: [],
        }
    },
    methods: {
        formatNumber: function (num) {
            return num < 10 ? '0' + num : num;
        },
        formatFileSize: function (fileSize) {
            if (fileSize < 1024) {
                return fileSize + 'B';
            } else if (fileSize < (1024 * 1024)) {
                var temp = fileSize / 1024;
                temp = temp.toFixed(2);
                return temp + 'KB';
            } else if (fileSize < (1024 * 1024 * 1024)) {
                var temp = fileSize / (1024 * 1024);
                temp = temp.toFixed(2);
                return temp + 'MB';
            }
        },
        formatTime: function (timestamp) {
            var date = new Date(parseInt(timestamp));
            var Y = date.getFullYear() + '-';
            var M = (date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1) + '-';
            var D = this.formatNumber(date.getDate()) + ' ';
            var h = this.formatNumber(date.getHours()) + ':';
            var m = this.formatNumber(date.getMinutes()) + ':';
            var s = this.formatNumber(date.getSeconds());
            return Y + M + D + h + m + s;
        },
        selectIndex: function (index) {
            this.index = index;
            switch (index) {
                case 0:
                    this.info = this.all;
                    break;
                case 1:
                    this.info = this.maid;
                    break;
                case 2:
                    this.info = this.chair;
                    break;
                case 3:
                    this.info = this.sound;
                    break;
            }
        }
    },
    mounted() {
        axios
            .get('MaidCustomPack/data/info.json')
            .then(response => {
                this.all = response.data;
                this.info = this.all;
                this.all.forEach(item => {
                    let type = item.type;
                    if (type.includes("maid")) {
                        this.maid.push(item)
                    }
                    if (type.includes("chair")) {
                        this.chair.push(item)
                    }
                    if (type.includes("sound")) {
                        this.sound.push(item)
                    }
                })
            })
            .catch(function (error) {
                alert(error)
            })
    }
});
