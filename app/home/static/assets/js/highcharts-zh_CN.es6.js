/**
 * Highcharts-zh_CN ES6 版本 plugins v1.2.0 (2020-07-03)
 *
 * (c) 2020 Jianshu Technology Co.,LTD (https://jianshukeji.com)
 *
 * Author : john@jianshukeji.com, Blue Monkey
 *
 * License: Creative Commons Attribution (CC)
 */

export default H => {

        let protocol = window.location.protocol;

        let defaultOptionsZhCn = {
                lang: {
                    // Highcharts
                    contextButtonTitle: '圖表導出菜單',
                    decimalPoint: '.',
                    downloadJPEG: "下載 JPEG 圖片",
                    downloadPDF: "下載 PDF 文件",
                    downloadPNG: "下載 PNG 文件",
                    downloadSVG: "下載 SVG 文件",
                    downloadXLS: "下載 XLS 文件",
                    drillUpText: "◁ 返回 {series.name}",
                    exitFullscreen: '退出全屏',
                    exportData: {
                        categoryDatetimeHeader: '時間',
                        categoryHeader: '類別'
                    },
                    openInCloud: '在 Highcharts Cloud 中打開',
                    invalidDate: '無效的時間',
                    loading: '加載中...',
                    months: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
                    navigation: {
                        popup: {
                            addButton: "新增",
                            arrowLine: "直線",
                            arrowRay: "射線",
                            arrowSegment: "線段",
                            background: "背景",
                            backgroundColor: "背景顏色",
                            backgroundColors: "背景顏色",
                            borderColor: "邊框顏色",
                            borderRadius: "圓角",
                            borderWidth: "邊框大小",
                            circle: "圓",
                            color: "顏色",
                            connector: "連接",
                            crooked3: "Crooked 3 line",
                            crooked5: "Crooked 5 line",
                            crosshairX: "豎直準星線",
                            crosshairY: "水平準星線",
                            editButton: "編輯",
                            elliott3: "Elliott 3 line",
                            elliott5: "Elliott 5 line",
                            fibonacci: "斐波納契",
                            fill: "填充顏色",
                            flags: "標誌",
                            fontSize: "字體大小",
                            format: "文本",
                            height: "高度",
                            horizo​​ ntalLine: "水平線",
                            infinityLine: "無限線",
                            innerBackground: "內背景",
                            label: "文字標籤",
                            labelOptions: "文字標籤配置",
                            labels: "文字標籤",
                            line: "線",
                            lines: "線條",
                            measure: "Measure",
                            measureX: "Measure X",
                            measureXY: "Measure XY",
                            measureY: "Measure Y",
                            name: "名字",
                            outerBackground: "外背景",
                            padding: "內間距",
                            parallelChannel: "並行通道",
                            pitchfork: "杈子",
                            ray: "射線",
                            rectangle: "矩形",
                            removeButton: "刪除",
                            saveButton: "保存",
                            segment: "段落",
                            series: "數據列",
                            shapeOptions: "圖形配置",
                            shapes: "圖形",
                            simpleShapes: "簡單圖形",
                            stroke: "線條顏色",
                            strokeWidth: "線條粗細",
                            style: "樣式",
                            title: "標題",
                            tunnel: "通道",
                            typeOptions: "詳情",
                            verticalArrow: "豎直箭頭",
                            verticalCounter: "豎直計數器",
                            verticalLabel: "豎直標籤",
                            verticalLine: "豎直線",
                            volume: "成交量"
                        }
                    },
                    noData: "暫無數據",
                    numericSymbols: null,
                    printChart: "打印圖表",
                    resetZoom: '重置縮放比例',
                    resetZoomTitle: '重置為原始大小',
                    shortMonths: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
                    thousandsSep: ',',
                    viewData: '查看數據表格',
                    viewFullscreen: '全屏查看',
                    weekdays: ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'],
                    viewData: '查看數據表格',
                    // Highstock
                    rangeSelectorFrom: '開始時間',
                    rangeSelectorTo: '結束時間',
                    rangeSelectorZoom: '範圍',

                    // Highmaps
                    zoomIn: '縮小',
                    zoomOut: '放大',
                },

                global: {
                    // 不使用 UTC時間
                    // useUTC: false,
                    //timezoneOffset: -8 * 60,
                    canvasToolsURL: protocol + '//cdn.hcharts.cn/highcharts/modules/canvas-tools.js',
                    VMLRadialGradientURL: protocol + +'//cdn.hcharts.cn/highcharts/gfx/vml-radial-gradient.png'
                },

                title: {
                    text: '圖表標題'
                },

                tooltip: {
                    dateTimeLabelFormats: {
                        millisecond: '%H:%M:%S.%L',
                        second: '%H:%M:%S',
                        minute: '%H:%M',
                        hour: '%H:%M',
                        day: '%Y-%m-%d',
                        week: '%Y-%m-%d',
                        month: '%Y-%m',
                        year: '%Y'
