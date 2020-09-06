/**
 * # DataManager
 * 
 * pull→this→push
 * 
 * recv→this→send
 * 
 * program→ui→page→block→line→inline
 */
// const { EventEmitter } = require('events')
class DataManager {
    #data
    constructor() {
        this.#data = {}
        document.addEventListener('pull', data => {
            console.log(data);
            AST.parse(this.#data, data.detail)
        })
        this.#data = AST.newElement('program')
        this.#data.data = {
            title: 'Era.js',
            footer: '@Miswanting',
            maxPages: 10,
            lastUi: '',
            ui: 'intro',
            msgs: [],
            blockMode: { type: 'line' },
            loadingTitle: 'Loading...',
            loadingText: 'If there is no connection for a long time,\nyou may need to manually start the backend.',
        }
        this.#data.data.menu = [
            {
                label: '文件',
                submenu: [
                    { label: '新建' },
                    { label: '打开' },
                    {
                        label: '最近打开的文件',
                        submenu: [
                            { label: 'File 1' },
                            { label: 'File 2' },
                            { label: 'File 3' }
                        ]
                    }
                ]
            },
            { label: '编辑' },
            { label: '窗口' },
            { label: '帮助' },
            { label: '+' }
        ]
        this.#data.children = {
            // 下可以呼出上
            console: AST.newElement('console'),
            pause: AST.newElement('pause'),
            game: AST.newElement('game'),
            intro: AST.newElement('intro'),
        }
    }
    /**
     * # getData
     * @returns {object}
     */
    getData() {
        return this.#data
    }
    send() {
        let event = new CustomEvent('send', { detail: data })
        document.dispatchEvent(event)
    }
    recv = (data) => {
        AST.parse(this.#data, data)
    }
}